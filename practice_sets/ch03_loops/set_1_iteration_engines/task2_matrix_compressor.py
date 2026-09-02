"""
Task 2: Algorithmic Logic Drill — Run-Length Matrix Compressor & Spatial Analyzer
Directory: practice_sets/ch03_loops/set_1_iteration_engines/
File: task2_matrix_compressor.py

Scenario & Business Problem:
You are building an embedded telemetry compression module for an IoT satellite camera. 
Raw sensor scans arrive as a 2D pixel grid of active sensor readings ("#") and background 
readings ("."). Before transmission over satellite uplinks, the matrix must be compressed 
row-by-row using run-length encoding, scanned for active vertical bounding coordinates, 
and analyzed for pixel density using raw algorithmic loops.

Constraints:
Strictly zero imports (no itertools, collections, re, or external compression libraries).

Raw Input Data:
6x7 2D Matrix of single-character strings:
Row 1: ["#", "#", "#", ".", ".", "#", "#"]
Row 2: ["#", ".", ".", ".", ".", ".", "#"]
Row 3: ["#", "#", "#", "#", "#", "#", "#"]
Row 4: [".", ".", "#", "#", "#", ".", "."]
Row 5: [".", ".", ".", "#", ".", ".", "."]
Row 6: [".", ".", ".", ".", ".", ".", "."]

Business Rules & System Logic:
1. Row-Level Compression & Density:
   - Compress each row using run-length encoding (e.g., Row 1 becomes "3#2.2#").
   - For each row, calculate Active Pixel Density percentage: (count of "#" / total characters) * 100. 
     Format to 1 decimal place (e.g., "71.4%").
2. Matrix-Level Spatial Summary:
   - Calculate total active pixels ("#") across the entire frame.
   - Calculate total background pixels (".") across the entire frame.
   - Calculate Overall Frame Active Ratio percentage: (Total Active / Total Pixels) * 100.
   - Active Bounding Row Span: Display the first and last row numbers that contain at least one active pixel.
3. Output Display:
   - Itemized row compression breakdown followed by the Matrix Spatial Telemetry Summary.
"""

RAW_MATRIX: list[list[str]] = [
    ["#", "#", "#", ".", ".", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"],
    [".", ".", "#", "#", "#", ".", "."],
    [".", ".", ".", "#", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]


def row_compression(rows: list[list[str]]) -> list:
    compressed_list: list = []

    for row in rows:
        count: int = 1
        compressed_str: str = ""

        current_char: str = row[0]
        for char in row[1:]:
            if char == current_char:
                count += 1
            else:
                compressed_str += f"{count}{current_char}"
                current_char = char
                count = 1
        compressed_str += f"{count}{current_char}"

        compressed_list.append(compressed_str)
    return compressed_list


def matrix_level(rows: list[list[str]]) -> list[int | list[str | int] | str]:
    row_active_list: list[int] = []
    row_density_list: list = []
    first_active_row: int = 0
    last_active_row: int = 0
    current_row_number: int = 1
    total_background_pixels: int = 0
    total_active_pixels: int = 0
    total_pixels: int = 0

    for row in rows:
        index: int = 0
        row_density: float = 0.0
        row_active_count: int = 0
        active_pixels: int = 0
        background_pixels: int = 0

        while index < len(row):
            total_pixels += 1
            if row[index] == "#":
                row_active_count += 1
                active_pixels += 1
            elif row[index] == ".":
                background_pixels += 1
            index += 1

        if "#" in row:
            if not first_active_row:
                first_active_row = current_row_number
            last_active_row = current_row_number
        current_row_number += 1

        # Calculating row density
        row_density_str: str = f"{(row_active_count / len(row) * 100):.1f}"
        total_active_pixels += active_pixels
        total_background_pixels += background_pixels
        row_active_list.append(row_active_count)
        row_density_list.append(row_density_str)

    # Calculating overall frame active density
    frame_ratio: str = f"{(total_active_pixels / total_pixels) * 100:.1f}"

    return [
        total_active_pixels,
        total_background_pixels,
        first_active_row,
        last_active_row,
        row_density_list,
        frame_ratio,
        row_active_list,
    ]


def main() -> None:
    compressed_list: list = row_compression(RAW_MATRIX)
    matrix_list: list = matrix_level(RAW_MATRIX)
    row_density: list[str] = matrix_list[4]
    row_active_pixels: list[int] = matrix_list[6]
    index: int = 0
    serial_no: int = 1
    full_dimension: int = len(RAW_MATRIX) * len(RAW_MATRIX[0])

    print(100 * "#")
    while index < len(RAW_MATRIX):
        print(f"""\
    {100 * "-"}
                            Row {serial_no} 
                 a. Row:                {RAW_MATRIX[index]}
                 b. Compressed String:  {compressed_list[index]}
                 c. Row Density:        {row_density[index]}%
                 d. Row Active Pixel:   {row_active_pixels[index]} out of {len(RAW_MATRIX[index])}
    {100 * "-"}
""")
        index += 1
        serial_no += 1

    print(f"""\
{100 * "="}
                 Summary
                 1. Full Dimension:     {full_dimension}
                 2. Total Active:       {matrix_list[0]}
                    Pixels
                 3. Total Background:   {matrix_list[1]}
                    Pixels
                 4. Overall Frame:      {matrix_list[5]}%
                    Ratio
                 5. Active Bounding:    from Row {matrix_list[2]} to
                    Row Span            Row {matrix_list[3]}
{100 * "="}
{100 * "#"}
""")


if __name__ == "__main__":
    main()

"""
EXPECTED TERMINAL OUTPUT:

####################################################################################################
    ----------------------------------------------------------------------------------------------------
                            Row 1 
                 a. Row:                ['#', '#', '#', '.', '.', '#', '#']
                 b. Compressed String:  3#2.2#
                 c. Row Density:        71.4%
                 d. Row Active Pixel:   5 out of 7
    ----------------------------------------------------------------------------------------------------

    ----------------------------------------------------------------------------------------------------
                            Row 2 
                 a. Row:                ['#', '.', '.', '.', '.', '.', '#']
                 b. Compressed String:  1#5.1#
                 c. Row Density:        28.6%
                 d. Row Active Pixel:   2 out of 7
    ----------------------------------------------------------------------------------------------------

    ----------------------------------------------------------------------------------------------------
                            Row 3 
                 a. Row:                ['#', '#', '#', '#', '#', '#', '#']
                 b. Compressed String:  7#
                 c. Row Density:        100.0%
                 d. Row Active Pixel:   7 out of 7
    ----------------------------------------------------------------------------------------------------

    ----------------------------------------------------------------------------------------------------
                            Row 4 
                 a. Row:                ['.', '.', '#', '#', '#', '.', '.']
                 b. Compressed String:  2.3#2.
                 c. Row Density:        42.9%
                 d. Row Active Pixel:   3 out of 7
    ----------------------------------------------------------------------------------------------------

    ----------------------------------------------------------------------------------------------------
                            Row 5 
                 a. Row:                ['.', '.', '.', '#', '.', '.', '.']
                 b. Compressed String:  3.1#3.
                 c. Row Density:        14.3%
                 d. Row Active Pixel:   1 out of 7
    ----------------------------------------------------------------------------------------------------

    ----------------------------------------------------------------------------------------------------
                            Row 6 
                 a. Row:                ['.', '.', '.', '.', '.', '.', '.']
                 b. Compressed String:  7.
                 c. Row Density:        0.0%
                 d. Row Active Pixel:   0 out of 7
    ----------------------------------------------------------------------------------------------------

====================================================================================================
                 Summary
                 1. Full Dimension:     42
                 2. Total Active:       18
                    Pixels
                 3. Total Background:   24
                    Pixels
                 4. Overall Frame:      42.9%
                    Ratio
                 5. Active Bounding:    from Row 1 to
                    Row Span            Row 5
====================================================================================================
####################################################################################################
"""