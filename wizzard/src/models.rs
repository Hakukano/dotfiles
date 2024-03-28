use std::collections::HashMap;

use serde::Deserialize;

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, Deserialize)]
enum Os {
    #[serde(rename = "default")]
    Default,
    #[serde(rename = "darwin")]
    Darwin,
}

#[derive(Deserialize)]
struct Model {
    pub configs: HashMap<String, String>,
}

/// name => os => modal
struct Models(HashMap<String, HashMap<Os, Model>>);
