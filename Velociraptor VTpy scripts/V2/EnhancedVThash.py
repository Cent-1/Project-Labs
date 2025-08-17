import vt

client = vt.Client("My_API_Key")

with open("/home/cent/Desktop/Hashs.txt", "r") as f, open("Reportdoc.txt", "w") as report:
    for line in f:
        hash_value = line.strip()
        file_object = client.get_object(f"/files/{hash_value}")
        stats = file_object.last_analysis_stats
        
        if stats["malicious"] > 0 or stats["suspicious"] > 0:
            output = (
                f"[!] {hash_value} Flagged - "
                f"Malicious: {stats['malicious']}, "
                f"Suspicious: {stats['suspicious']}"
            )
            print(output)
            report.write(output + "\n")

client.close()
