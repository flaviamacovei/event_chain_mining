from data.extract import extract
from data.transform import transform

def main():
    print("Hello from event-chain-mining!")
    raw_data = extract("data/data_files/preprocessed_short.txt")
    transformed_data = transform(raw_data)
    print(transformed_data)


if __name__ == "__main__":
    main()
