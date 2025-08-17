import vt

client = vt.Client("My_API_key")

with open("/home/cent/Desktop/Hashs.txt", "r") as f:
    for line in f:
        hash_value = line.strip()
        file_object = client.get_object(f"/files/{hash_value}")
        print(f"{hash_value}: {file_object.last_analysis_stats}")

client.close()
