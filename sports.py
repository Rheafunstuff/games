badminton={"Jim", "Henry", "Orla", "Olaf", "Timmy", "Jake"}
print("Badminton players :", badminton)
soccer={"Jack", "Timmy", "Yasmin", "Nancy", "Orla", "David"}
print("Soccer players : ", soccer)

Both_bad_soc= (badminton.intersection(soccer))
print("Players playing both badminton and soccer :", Both_bad_soc)

Bad_or_soc_but_not_both= (badminton.symmetric_difference(soccer))
print("Players playing badminton or soccer but not both :" , Bad_or_soc_but_not_both)

Bad_only= (badminton.difference(Both_bad_soc))
print("Players playing only badminton :" , Bad_only)