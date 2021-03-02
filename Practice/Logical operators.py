# We use when we have multiple conditions
has_highincome=True
has_goodcredit=True
has_criminalrecord=False

if has_highincome and has_goodcredit:
    print("Eligible for loan")
if has_highincome or has_goodcredit:
    print("Eligible for loan")
if has_goodcredit and not has_criminalrecord:
    print("Eligible for loan")
