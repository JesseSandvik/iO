from dataclasses import dataclass
from datetime import datetime
from packaging.version import Version
from typing import List, Optional

@dataclass(frozen=True)
class PluginMetadata:
    entry_point: str
    name: str
    description: str
    version: str
    author: str
    required_python_version: str
    last_updated: datetime
    user_enabled: bool = False
    compatible_application_versions: Optional[List[str]] = None
    dependencies: Optional[List[str]] = None
    tags: Optional[List[str]] = None

    def __init__(
            self,
            entry_point: str,
            name: str,
            description: str,
            version: str,
            author: str,
            required_python_version: str,
            user_enabled: bool = False,
            compatible_application_versions: Optional[List[str]] = None,
            dependencies: Optional[List[str]] = None,
            tags: Optional[List[str]] = None
        ):
        object.__setattr__(self, "entry_point", entry_point)
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "description", description)
        object.__setattr__(self, "version", version)
        object.__setattr__(self, "author", author)
        object.__setattr__(self, "required_python_version", required_python_version)
        object.__setattr__(self, "user_enabled", user_enabled)
        object.__setattr__(self, "last_updated", datetime.now().replace(microsecond=0).isoformat())
        object.__setattr__(self, "compatible_application_versions", compatible_application_versions)
        object.__setattr__(self, "dependencies", dependencies)
        object.__setattr__(self, "tags", tags)

    def version_changed(self, new_version: str) -> bool:
        return Version(self.version) != Version(new_version)
    
    def has_compatible_python_version(self, current_python_version: str) -> bool:
        return Version(current_python_version) >= Version(self.required_python_version)

    def has_compatible_application_version(self, application_version: str) -> bool:
        for compatible_version in self.compatible_application_versions:
            if Version(application_version) == Version(compatible_version):
                return True
        return False
