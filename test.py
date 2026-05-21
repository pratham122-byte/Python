monday={"pratham","kumar","singh"}
tuesday={"pratham","gaurav","singh"}
common_days=monday.intersection(tuesday)
onlymonday= monday-tuesday
onlytuesday=tuesday-monday
print("student who attend only on monday",onlymonday)
print("student who ateend on tuesday",    onlytuesday)
print("who attend the both monday and tuesday",common_days)