const CATEGORIES = {
    'E': 'Engine',
    'T': 'Transmission',
    'U': 'ECU',
    'B': 'Body',
    'I': 'Interior',
    'O': 'Other',
    'S': 'Suspension',
}

export function getCategoryValue(key) {
    return CATEGORIES[key];
}