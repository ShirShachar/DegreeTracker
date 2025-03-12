import re


def parse_transcript(file_path):
    """
    Reads a transcript text file and extracts course details.
    """
    courses = []
    current_semester = None

    # Regex for course details
    course_pattern = re.compile(
        r"([A-Z]{2,4})\s+([A-Z0-9]+)\s+(.+?)\s+(\d+\.\d{2})\s+([A-FP\+W]+)")

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # Detect semester changes
            if re.match(r"(Spring|Summer|Fall) \d{4}", line):
                current_semester = line.strip()

            # Extract courses
            match = course_pattern.match(line)
            if match and current_semester:
                subject, course_number, title, credits, grade = match.groups()
                courses.append({
                    "Semester": current_semester,
                    "Course Code": f"{subject} {course_number}",
                    "Title": title.strip(),
                    "Credits": float(credits),
                    "Grade": grade
                })

    return courses
