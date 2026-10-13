import os
import random
import time
from datetime import date
from faker import Faker

def generate_dataset(
    output_filename: str = "input.txt",
    keys_filename: str = "test_keys.txt",
    total_records: int = 1_000_000,
    buffer_size_lines: int = 50_000,
):
    start_time = time.perf_counter()
    fake = Faker("ru_RU")

    start_ord = date(2020, 1, 1).toordinal()
    end_ord = date(2026, 12, 31).toordinal()
    date_pool = [
        f"{d.day:02d}.{d.month:02d}.{d.year}"
        for d in (date.fromordinal(o) for o in range(start_ord, end_ord + 1))
    ]

    pool_size = 3_000
    last_names_m = [fake.last_name_male() for _ in range(pool_size // 2)]
    first_names_m = [fake.first_name_male() for _ in range(pool_size // 2)]
    middle_names_m = [fake.middle_name_male() for _ in range(pool_size // 2)]

    last_names_f = [fake.last_name_female() for _ in range(pool_size // 2)]
    first_names_f = [fake.first_name_female() for _ in range(pool_size // 2)]
    middle_names_f = [fake.middle_name_female() for _ in range(pool_size // 2)]

    fio_pool = [
        f"{ln} {fn} {mn}"
        for ln, fn, mn in zip(last_names_m, first_names_m, middle_names_m)
    ] + [
        f"{ln} {fn} {mn}"
        for ln, fn, mn in zip(last_names_f, first_names_f, middle_names_f)
    ]

    choice = random.choice
    randint = random.randint
    lines = []

    duplicate_target = ("15.05.2023", "Иванов Иван Иванович", 777777)
    dup_row = f"{duplicate_target[0]},{duplicate_target[1]},{duplicate_target[2]}\n"
    dup_positions = {50, 500_000, 950_000}

    with open(output_filename, "w", encoding="utf-8", buffering=8 * 1024 * 1024) as f:
        for current_idx in range(1, total_records + 1):
            if current_idx in dup_positions:
                lines.append(dup_row)
            else:
                lines.append(f"{choice(date_pool)},{choice(fio_pool)},{randint(100_000, 9_999_999)}\n")

            if len(lines) >= buffer_size_lines:
                f.writelines(lines)
                lines.clear()

        if lines:
            f.writelines(lines)

    elapsed = time.perf_counter() - start_time
    file_size_mb = os.path.getsize(output_filename) / (1024 * 1024)
    print(f"Готово за {elapsed:.2f} сек. Размер: {file_size_mb:.2f} МБ")

    with open(keys_filename, "w", encoding="utf-8") as kf:
        kf.write(f"duplicate_lines: {sorted(dup_positions)}\n")
        kf.write(f"duplicate_key: {dup_row.strip()}\n")
        kf.write("missing_key: 01.01.1970,Несуществующий Пользователь Тестович,99999999\n")

if __name__ == "__main__":
    generate_dataset()
