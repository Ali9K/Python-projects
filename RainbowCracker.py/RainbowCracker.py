import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    Dict = {}
    m = hashlib.sha256("0000".encode())
    n = m.hexdigest()
    Dict[n] = "0000"

    for i in range(1000, 10000):
        i = str(i)
        m = hashlib.sha256(i.encode())
        n = m.hexdigest()
        Dict[n] = i

    with open(input_file_name) as x:
        reader = csv.reader(x)
        with open(output_file_name, 'w', newline='') as y:
            writer = csv.writer(y)
            
            for row in reader:
                name = row[0]
                hash_value = row[1]

                if hash_value in Dict:
                    writer.writerow([name, Dict[hash_value]])
