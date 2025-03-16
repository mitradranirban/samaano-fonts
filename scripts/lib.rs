use fontdue::layout::{Layout, TextStyle};
use fontdue::Font;
use std::fs;
use std::collections::HashMap;
use ttf_parser::{Face, VariationAxis, ValueRecord};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let font_data = fs::read("*.ttf")?; // Replace with your font file
    let face = Face::parse(&font_data, 0)?;

    if let Some(stat) = face.stat() {
        let axes: Vec<VariationAxis> = stat.axes().collect();
        let named_instances = stat.named_instances().collect::<Vec<_>>();

        println!("Axes:");
        for axis in &axes {
            println!(
                "  Tag: {}, Name: {}, Min: {}, Default: {}, Max: {}",
                axis.tag,
                face.localized_string(axis.name_id).unwrap_or_default(),
                axis.min_value,
                axis.default_value,
                axis.max_value
            );
        }

        println!("\nNamed Instances:");
        for instance in &named_instances {
            println!(
                "  Name: {}",
                face.localized_string(instance.name_id).unwrap_or_default()
            );
            println!("  Coordinates:");
            for record in instance.values() {
                if let ValueRecord::Coordinate(coord) = record {
                    if let Some(axis) = axes.iter().find(|a| a.tag == record.axis_tag()) {
                        println!(
                            "    {}: {}",
                            face.localized_string(axis.name_id).unwrap_or_default(),
                            coord
                        );
                    }
                }
            }
            println!("---");
        }

        println!("\nAll Possible Axis Combinations and Named Instances:");

        generate_all_combinations(&face, &axes, &named_instances);
    } else {
        println!("No STAT table found in the font.");
    }

    Ok(())
}

fn generate_all_combinations(face: &Face, axes: &[VariationAxis], named_instances: &[ttf_parser::NamedInstance]) {
    let mut combinations: Vec<HashMap<u32, f32>> = vec![HashMap::new()];

    for axis in axes {
        let mut new_combinations = Vec::new();
        for combination in &combinations {
            new_combinations.push(combination.clone());

            let mut min_combination = combination.clone();
            min_combination.insert(axis.tag, axis.min_value);
            new_combinations.push(min_combination);

            let mut max_combination = combination.clone();
            max_combination.insert(axis.tag, axis.max_value);
            new_combinations.push(max_combination);

            if axis.min_value != axis.default_value && axis.max_value != axis.default_value{
                let mut default_combination = combination.clone();
                default_combination.insert(axis.tag, axis.default_value);
                new_combinations.push(default_combination);
            }
        }
        combinations = new_combinations;
    }

    for combination in &combinations {
        println!("Combination:");
        for (tag, value) in combination {
            if let Some(axis) = axes.iter().find(|a| a.tag == *tag) {
                println!(
                    "  {}: {}",
                    face.localized_string(axis.name_id).unwrap_or_default(),
                    value
                );
            }
        }
        println!("---");
    }

    for instance in named_instances{
        println!("Named Instance: {}", face.localized_string(instance.name_id).unwrap_or_default());
        println!("Coordinates:");
        for record in instance.values() {
                if let ValueRecord::Coordinate(coord) = record {
                    if let Some(axis) = axes.iter().find(|a| a.tag == record.axis_tag()) {
                        println!(
                            "    {}: {}",
                            face.localized_string(axis.name_id).unwrap_or_default(),
                            coord
                        );
                    }
                }
            }
        println!("---");
    }
}