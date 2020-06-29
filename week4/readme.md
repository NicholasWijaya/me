TODO: Reflect on what you learned this week and what is still unclear.

\n = linefeed (prints the stuff after this on the next line)
\r = carriage return (basically also used for printing stuff on the next line)
\’ = print a single quote ( ‘ ) in your text
\” = print a double quote ( “ ) in your text
\\ = print a backslash ( \ ) in your text

open(file_path,mode)
    mode:   'r' - reading only. error is file doesn't exist (default)
            '+' - read and write
            'w' - write only. creates file if it doesn't exist
            'a' - append only. creates file if it doesn't exist
            'x' - creates file. fails if file already exists.

json.load(item) - convert item into JSON data