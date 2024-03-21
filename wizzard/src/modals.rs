use std::collections::HashMap;

use serde::Deserialize;

#[derive(Deserialize)]
struct Modal {}

/// name => os => modal
struct Modals(HashMap<String, HashMap<String, Modal>>);
