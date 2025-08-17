import vt

client = vt.Client("My_API_Key")

with open("/home/cent/Desktop/Hashs.txt", "r") as f, open("Reportdoc.txt", "w") as report:
    for line in f:
        hash_value = line.strip()
        try:
            file_object = client.get_object(f"/files/{hash_value}")
            stats = file_object.last_analysis_stats
            malicious = stats.get("malicious", 0)
            suspicious = stats.get("suspicious", 0)

            if malicious > 0 or suspicious > 0:
                output = f"[!] {hash_value} Flagged - Malicious: {malicious}, Suspicious: {suspicious}"
                print(output)
                report.write(output + "\n")

        except Exception as e:
            error_message = f"[!] Error with hash {hash_value} - {str(e)}"
            print(error_message)
            report.write(error_message + "\n")

client.close()
