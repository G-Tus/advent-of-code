use std::fs::File;
use std::io::{self, BufReader, Read};

fn main() -> io::Result<()> {
    let file = File::open("../input.txt")?;
    let reader = BufReader::new(file);

    let mut floor = 0;
    let mut position = 0;
    let mut first: Option<i32> = None;

    for char in reader.bytes() {
        position += 1;
        let step = char? as char;
        match step {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => continue,          
        }

        if floor == -1 && first.is_none() {
            first = Some(position);
        }
    }

    println!("Santa ends up at floor: {}", floor);
    println!("Santa enter basements at position: {:?}", first);

    Ok(())
}