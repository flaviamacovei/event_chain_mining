from data.extract import extract
from data.transform import transform
from data.load import load

def main():
    print("Hello from event-chain-mining!")
    raw_data = extract("data/data_files/preprocessed_short.txt")
    transformed_data = transform(raw_data)
    loaded_data = load(transformed_data)
    print(loaded_data)


if __name__ == "__main__":
    main()
