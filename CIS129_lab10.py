def check_protect(amount):
    formatted_amount = f"{amount:>10}"
    protected_amount = formatted_amount.replace(" ", "*")
    return protected_amount

# Example usage:
print(check_protect("$123.45"))  # Output: ***$123.45