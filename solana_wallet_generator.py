import multiprocessing
import time
import json
import os
import base58
from solders.keypair import Keypair

NUM_PROCESSES = multiprocessing.cpu_count()  # Use all CPU cores

# Save wallet to JSON file
def save_wallet(address, private_key_b58):
    file_path = "solana_wallets.json"

    # Load existing wallets
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                wallets = json.load(file)
            except json.JSONDecodeError:
                wallets = []
    else:
        wallets = []

    # Append new wallet
    wallets.append({"Address": address, "Private_Key": private_key_b58})

    # Save updated list
    with open(file_path, "w") as file:
        json.dump(wallets, file, indent=4)

# Generate wallet with multiprocessing
def generate_wallet(shared_found, prefix, suffix):
    while not shared_found.value:  # Keep generating until a wallet is found
        kp = Keypair()
        address = str(kp.pubkey())

        if address.startswith(prefix) and address.endswith(suffix):
            shared_found.value = True  # Stop all processes

            # Full 64-byte private key (Secret Key + Public Key)
            full_private_key = kp.to_bytes()  # 64 bytes
            private_key_b58 = base58.b58encode(full_private_key).decode()  # Base58 encode

            print("\n✅ Wallet Found!")
            print(f"🔑 Address: {address}")
            print(f"🔐 Private Key (Phantom Import Format): {private_key_b58}")

            save_wallet(address, private_key_b58)  # Save wallet to file
            return

# Main function to ask user input & control execution
def main():
    while True:
        # Ask user for prefix & suffix
        prefix = input("Enter wallet prefix (optional): ").strip()
        suffix = input("Enter wallet suffix (optional): ").strip()

        print(f"\n🚀 Searching for Solana wallet with prefix '{prefix}' and suffix '{suffix}'...\n")
        start_time = time.time()
        found = multiprocessing.Value('b', False)  # Shared flag to stop all processes

        processes = []
        for _ in range(NUM_PROCESSES):
            p = multiprocessing.Process(target=generate_wallet, args=(found, prefix, suffix))
            p.start()
            processes.append(p)

        try:
            for p in processes:
                p.join()
        except KeyboardInterrupt:
            print("\n❌ Stopped by user.")

        elapsed_time = time.time() - start_time
        print(f"\n✅ Search completed in {elapsed_time:.2f} seconds")

        # Ask if the user wants to generate another wallet
        choice = input("\n🔄 Generate another wallet? (y/n): ").strip().lower()
        if choice != 'y':
            print("🚪 Exiting...")
            break

if __name__ == "__main__":
    main()
