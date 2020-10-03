EXTENSIONS = {
    "PYTHON": (".py", ".pyc", ".pyo"),
    "Web": (".html5", ".html", ".htm", ".xhtml", ".css", ".js"),
    "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg","svg",".heif", ".psd"),
    "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",".mng",".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
    "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",".ods",".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt","pptx"),
    "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip"),
    "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",".mp3", ".md",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
    "PLAINTEXT": (".txt", ".in", ".out"),
    "Shell": (".sh", ".fish", ".zsh", ".ps1", ".csh"),
    "OS": (".deb", ""),
    "PDF": (".pdf", ""),
    "EXE": (".exe", ""),
    "Folders": (""),
    "Other-Files": (".", "")
}
file_formats = {
    file: directory
    for directory, file_extensions in EXTENSIONS.items()
    for file in file_extensions
}