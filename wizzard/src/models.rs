use std::collections::HashMap;

use serde::Deserialize;

#[derive(Deserialize)]
struct Model {}

/// name => os => modal
struct Models(HashMap<String, HashMap<String, Model>>);
