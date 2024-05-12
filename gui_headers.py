gr_color = '\033[0;32m'
bl_color = '\033[0;34m'
end_color = '\033[0m'

def main_menu_header_ascii():
    print(rf"""
    {gr_color}     ______      ____  {bl_color}/{end_color}{gr_color}         __ 
    {gr_color}    / ____/___ _/ / /_{bl_color}//{end_color}{gr_color}  __  __/ /_
    {gr_color}   / /_  / __ `/ / / {bl_color}//{end_color}{gr_color}\/ / / / __/
    {gr_color}  / __/ / /_/ / / / {bl_color}/-/{end_color}{gr_color} / /_/ / /_  
    {gr_color} /_/    \____/_/_/\_{bl_color}//{end_color}{gr_color}_/\____/\__/  
                       {bl_color}/{end_color}""")

def header(text: str) -> None:
    print(f'{gr_color}|------------------------------------------------|')
    print(f'> {text}')
    print(f'|------------------------------------------------|{end_color}')