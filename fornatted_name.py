def get_fornatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_fornatted_name('jimi', 'hendrix')
print(musician)
