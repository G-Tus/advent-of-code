use std::fs::File;
use std::io::{self, BufRead, BufReader};
use regex::Regex;

fn main() -> io::Result<()> {
    let file = File::open("../input.txt")?;
    let reader = BufReader::new(file);

    let mut total = 0;
    let digit_regex = Regex::new(r"\d").unwrap();

    for line_result in reader.lines() {
        let line = line_result?;
        let mut digits = Vec::new();

        for cap in digit_regex.captures_iter(&line) {
            digits.push(cap.get(0).unwrap().as_str());
        }

        if let (Some(first), Some(last)) = (digits.first(), digits.last()) {
            let result = format!("{}{}", first, last).parse::<i32>().unwrap();
            total += result;
        }
    }

    println!("Calibration value: {}", total);

    Ok(())
}

