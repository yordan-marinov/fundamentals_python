from collections import defaultdict


def collect_data():
    companies = defaultdict(list)
    while True:

        data = input()
        if data == "End":
            return dict(
                sorted(companies.items())
            )

        company_name, employee_id = data.split(' -> ')

        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)


for company, id_numbers in collect_data().items():
    print(company)
    for id_number in id_numbers:
        print(f"-- {id_number}")
