use std::fs::File;
use std::io::{self, BufReader, Read};

fn main() -> io::Result<()> {
    let file = File::open("../input.txt")?;
    let reader = BufReader::new(file);

    let mut floor = 0;

    for char in reader.bytes() {
        let step = char? as char;
        match step {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => continue,          
        }
    }

    println!("Santa ends up at floor: {}", floor);

    Ok(())
}