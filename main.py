from data.extract import extract

def main():
    print("Hello from event-chain-mining!")
    raw_data = extract("data/data_files/preprocessed_short.txt")
    print(raw_data)


if __name__ == "__main__":
    main()
