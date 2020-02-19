"""View 层所有 RBAC 的相关错误"""

from ...core import error as _error


class AuthenticationError(_error.Error):
    """身份验证错误"""
    code = 13001
    description = "身份验证错误"


class AuthenticationDisabled(AuthenticationError):
    """该身份验证方式被禁用"""
    code = 13002
    description = "该身份验证方式被禁用"


class InvalidExceptionAccessPonint(_error.Error):
    """前端传入的例外用户组无法识别/用户ID错误"""
    code = 13003
    description = "传入的例外用户组无法被识别/用户ID错误"


class AccessPointNameConflicting(_error.Error):
    """访问点名称冲突"""
    code = 13004
    description = "访问点名称冲突"


class UndefinedUserIndex(_error.Error):
    """未定义的用户索引类型"""
    code = 13005
    description = "未定义的用户索引类型"
