def check_access(files, queries):
    access_rights = {}
    for file, rights in files.items():
        access_rights[file] = set(rights.split())

    results = []
    for query in queries:
        operation, file = query.split()
        if operation in access_rights.get(file, set()):
            results.append("OK")
        else:
            results.append("Access denied")
    return results

if __name__ == "__main__":
    files_input = {
        "helloworld.exe": "R X",
        "pinglog": "W R",
        "nya": "R",
        "goodluck": "X W R"
    }
    queries_input = [
        "read nya",
        "write helloworld.exe",
        "execute nya",
        "read pinglog",
        "write pinglog"
    ]

    expected_output = [
        "OK",
        "Access denied",
        "Access denied",
        "OK",
        "OK"
    ]

    results = check_access(files_input, queries_input)
    for result, expected in zip(results, expected_output):
        print(f"Result: {result}, Expected: {expected}")

