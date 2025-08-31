import dim_utils

print("CMU Block Dimension Checker")
print("Enter a length (e.g. 6'4\", 76\", 19). Type 'q' to quit.", end="\n\n")

while True:
    try:
        user_input = input("Enter a length: ").strip()
        if user_input.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        total_inches = dim_utils.parse_input(user_input)
        is_block, next_b, prev_b = dim_utils.check_block_dimension(total_inches)

        if prev_b:
            print(f"🡠 Previous block dimension: {dim_utils.format_inches_to_ft_in(prev_b)}")
        else:
            print(f"🡠 No smaller block dimension.")

        if is_block:
            print(f"✓ {dim_utils.format_inches_to_ft_in(total_inches)} is a block dimension.")
        else:
            print(f"✗ {dim_utils.format_inches_to_ft_in(total_inches)} is not a block dimension.")

        print(f"🡢 Next block dimension: {dim_utils.format_inches_to_ft_in(next_b)}\n")

    except ValueError as e:
        print(f"✗ {e}\n")