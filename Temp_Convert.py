def main ():
    unit = input("What unit do you want to convert(example: celsius):")
    temp = input("What is your temperature value(just the number):")
    if unit == "celsius" or unit == "C" or unit == "c" or unit == "°C" or unit == "Celsius":
        temp1 = ((int(temp) * (9/5))+32);
        temp2 = ((int(temp) + 273.15))
        print("{}°F".format(int(temp1)))
        print("{}K".format(int(temp2)))
    elif unit == "farenheit" or unit == "F" or unit == "f" or unit == "°F" or unit == "Fahrenheit":
        temp1 = ((int(temp) - 32)*(5/9));
        temp2 = ((int(temp) - 32)*(5/9)) + 273.15;
        print("{}°C".format(int(temp1)));
        print("{}K".format(int(temp2)))
    elif unit == "kelvin" or unit == "K" or unit == "k" or unit == "Kelvin":
        temp1 = ((int(temp) - 273.15))
        temp2 = ((int(temp) - 32)*(5/9)) - 273.15
        print("{}°C".format(int(temp1)));
        print("{}°F".format(int(temp2)));
    else:
        print("Unit not available in this converter(make sure the unit is written correctly and that temperature only has the number and not the unit)");

main()
