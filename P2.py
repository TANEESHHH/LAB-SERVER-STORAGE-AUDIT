# Read the inventory, organise it in a suitable structure, and print
# the required storage-audit report.
def parse_record(line):
    """Return the record dictionary for one inventory line."""
    listline = line.split(",")
    topper = listline[0].split("/")
    reqdict = {}
    
    reqdict["top_folder"] = topper[0]
    reqdict["full_filename"] = listline[0] + "/" + listline[1]
    reqdict["size"] = int(listline[2])
    reqdict["days_since_access"] = int(listline[3])
    return reqdict

    pass
def folder_totals(files):
    """Return a dictionary: top-level folder -> total size of its files."""
    reqdict = {}
    topfolderlist = []
    sizelist = []
    for record in files:
        topfolderlist.append(record["top_folder"])
        sizelist.append(record["size"])
    for i in range(len(topfolderlist)):
        reqdict[topfolderlist[i]] = 0
    for i in range(len(sizelist)):
        reqdict[topfolderlist[i]] += sizelist[i]
        
        
    return reqdict
    
    pass
def largest_folder(totals):
    """Return the folder with the largest total. A tie goes to the alphabetically first name."""
    return max(sorted(totals), key=totals.get)
    pass
def archive_candidates(files, minimum_size_mb, stale_after_days):
    """Return the candidate records, largest first, then by full file path."""
    candrecords = []
    for record in files:
        if (record["size"] >= minimum_size_mb) and (record["days_since_access"] >= stale_after_days):
            candrecords.append(record)
            candrecords = sorted(candrecords, key= lambda record: (-record["size"],record["full_filename"]))
    return candrecords            
            
    pass

n = int(input().strip())  

lines = [input().strip() for _ in range(n)]
# reads the next n lines of records

minimum_size_mb,stale_after_days = input().strip().split(",")
files = [parse_record(line) for line in lines]
totals = folder_totals(files)
lgstfldr = largest_folder(totals)
candrecords = archive_candidates(files, int(minimum_size_mb), int(stale_after_days))
arch = []
total = 0
for record in candrecords:
    arch.append(record["full_filename"])
    total += record["size"]
print(f"Largest top-level folder: {lgstfldr}")
print(f"Archive candidates: {arch}")
print(f"Recoverable storage: {total} MB")
    
    
    
    




