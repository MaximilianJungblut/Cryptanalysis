import pandas as pd
from CaesarsCipher import Caesar


def shift_digits(s: str, p: int) -> str:
    p = p % 10
    result = []
    for string_digit in s:
        new_digit = (ord(string_digit) - ord('0') + p) % 10
        result.append(chr(ord('0') + new_digit))
    return "".join(result)


def main(lat: float, long: float):
    lat_int_str, lat_dec_str = str(object=lat).split(sep=".")
    long_int_str, long_dec_str = str(object=long).split(sep=".")

    c_matrix = {
        "long": [str(object=long_p) for long_p in range(0,10)]
    }

    for lat_p in range(0,10):
        for long_p in range(0,10):
            c_lat_dec_str = shift_digits(s=lat_dec_str, p=lat_p)
            c_long_dec_str = shift_digits(s=long_dec_str, p=long_p)
            c_coords = f"{lat_int_str}.{c_lat_dec_str}, {long_int_str}.{c_long_dec_str}"
            if str(object=lat_p) not in c_matrix:
                c_matrix[str(object=lat_p)] = []
            c_matrix[str(object=lat_p)].append(c_coords)
    
    df = pd.DataFrame(data=c_matrix)
    df.to_csv(path_or_buf="obfuscation_matrix.csv", index=False)


if "__main__" == __name__:
    lat = 35.01455380292978
    long = -106.68627789365152
    main(lat=lat, long=long)