from flask import Flask, redirect, render_template, request, url_for
import requests
from datetime import datetime


class explorer():

    def __init__(self):
        self.node = input("Please input the address of a blockchain node:\n")
        self.chain = self.get_chain()
        self.recenttx = self.get_recent_transactions()

    def total_address_sent(self, address):
        all_transactions_amounts = 0
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['sender'] == address:
                    all_transactions_amounts += transaction['amount']
        return all_transactions_amounts

    def total_address_received(self, address):
        all_transactions_amounts = 0
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['recipient'] == address:
                    all_transactions_amounts += transaction['amount']
        return all_transactions_amounts

    def get_recent_blocks(self):
        blocks = []
        itercount = 0
        for block in reversed(self.chain):
            blocks.append(block)
            itercount += 1
            if itercount == 15:
                return blocks

    def get_block_from_index(self, index):
        for block in reversed(self.chain):
            height = block['index']
            if int(height) == int(index):
                return block


    def total_address_transactions(self, address):
        all_transactions = []
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['recipient'] == address or transaction['sender'] == address:
                    all_transactions.append(transaction)
        return all_transactions

    def get_recent_transactions(self):
        recent_transactions = []
        itercount = 0
        for block in reversed(self.chain):
            for transaction in block['transactions']:
                recent_transactions.append(transaction)
                itercount += 1
                if itercount == 15:
                    print(f'got 10 transactions {recent_transactions}')
                    return recent_transactions

    def recent_tx_amount(self, transaction):
        tx_amount = transaction['amount']
        return tx_amount

    def recent_tx_time(self, transaction):
        tx_time = transaction['time_submitted']
        return datetime.utcfromtimestamp(tx_time).strftime('%Y-%m-%d %H:%M:%S')

    def recent_tx_hash(self, transaction):
        tx_hash = transaction['transaction_hash']
        return tx_hash

    def truncate_hash(self, hash):
        trun_hash = f'{hash[:35]}...'
        return trun_hash

    def unconfirmed_txs(self):
        response = requests.get(f'http://{self.node}/mempool')
        mempool = response.json()
        unconfirmed = 0
        for transaction in mempool:
            unconfirmed += 1
        return unconfirmed

    def get_block_time(self, block):
        block_time = block['timestamp']
        return block_time

    def get_block_time_human(self, block):
        block_time = block['timestamp']
        return datetime.utcfromtimestamp(block_time).strftime('%Y-%m-%d %H:%M:%S')

    def get_last_block_time(self):
        last_block = self.chain[-1]
        time_submitted = last_block['timestamp']
        return datetime.utcfromtimestamp(time_submitted).strftime('%Y-%m-%d %H:%M:%S')

    def get_chain(self):
        response = requests.get(f'http://{self.node}/chain')
        chain = response.json()['chain']
        return chain

    def get_block_height(self):
        response = requests.get(f'http://{self.node}/chain')
        length = response.json()['length']
        return length

    def get_last_proof(self):
        response = requests.get(f'http://{self.node}/proof')
        return response.json()

    def total_transactions(self):
        total_transactions = 0
        for block in self.chain:
            for transaction in block['transactions']:
                total_transactions += 1
        return total_transactions

    def get_block_index_from_transaction(self, tx):
        hash_to_find = tx['transaction_hash']
        for block in self.chain:
            for transaction in block['transactions']:
                tx_hash = transaction['transaction_hash']
                if tx_hash == hash_to_find:
                    return block['index']

    def get_tx_from_hash(self, tx_hash):
        for block in self.chain:
            for transaction in block['transactions']:
                hash = transaction['transaction_hash']
                if hash == tx_hash:
                    return transaction

    def get_index_from_hash(self, hash):
        for block in self.chain:
            block_hash = block['current_hash']
            if hash == block_hash:
                return block['index']


    def total_addresses(self, mode):
        address_no = 0
        unique_addresses = []
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['recipient'] not in unique_addresses:
                    unique_addresses.append(transaction['recipient'])
                    address_no += 1
                if transaction['recipient'] in unique_addresses:
                    continue
        if mode == "number":
            return address_no

        if mode == "unique":
            return unique_addresses


explorer = explorer()

app = Flask(__name__)


@app.route("/block/<index>")
def block_view(index):
    block = explorer.get_block_from_index(index)
    print(block)
    return render_template("block.html",
                           index=index,
                           block=block,
                           explorer=explorer
                           )


@app.route("/txs/<tx>")
def transaction_view(tx):
    txs = explorer.get_tx_from_hash(tx)

    return render_template(
        "txs.html",
        explorer=explorer,
        tx=txs
    )


@app.route("/addrs/<addr>")
def address_view(addr):
    all_transactions = explorer.total_address_transactions(addr)
    total_transactions = len(all_transactions)
    total_received = explorer.total_address_received(addr)
    total_sent = explorer.total_address_sent(addr)
    balance = total_received - total_sent
    sent_transactions = []
    received_transactions = []

    for transaction in all_transactions:
        if transaction['sender'] == addr:
            sent_transactions.append(transaction)
        if transaction['recipient'] == addr:
            received_transactions.append(transaction)

    print(received_transactions)
    print(sent_transactions)



    return render_template("addrs.html",
                           addr=addr,
                           explorer=explorer,
                           all_transactions=reversed(all_transactions),
                           sent_transactions=sent_transactions,
                           received_transactions=received_transactions,
                           total_transactions=total_transactions,
                           total_received=total_received,
                           total_sent=total_sent,
                           balance=balance
                           )


@app.route("/")
def home():
    length = explorer.get_block_height()
    last_proof = explorer.get_last_proof()
    addresses = explorer.total_addresses(mode="number")
    mempool = explorer.unconfirmed_txs()
    last_time = explorer.get_last_block_time()
    total_tx = explorer.total_transactions()
    recent_txs = explorer.get_recent_transactions()
    recent_blocks = explorer.get_recent_blocks()
    explorer.chain = explorer.get_chain()

    return render_template(
        # Template
        "index.html",
        # front page data
        length=length,
        last_proof=last_proof,
        total_address_num=addresses,
        mempool_tx_num=mempool,
        last_block_time=last_time,
        total_tx_num=total_tx,
        explorer=explorer,
        recent_txs=recent_txs,
        recent_blocks=recent_blocks
    )


@app.route("/search", methods=['GET'])
def search():
    query = request.args.get("query")
    print(query)
    addresses = explorer.total_addresses(mode="unique")
    if query in addresses:
        return redirect(f'/addrs/{query}')

    if len(query) == 64:
        return redirect(f'/txs/{query}')

    try:
        if int(query) <= explorer.get_block_height():
            return redirect(f'/block/{query}')
    except:
        pass




if __name__ == "__main__":
    app.run(host='0.0.0.0')
