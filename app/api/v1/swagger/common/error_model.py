from flask_restx import fields
from app.application.settings.api_setting import api


class ErrorModel:
    @staticmethod
    def error_model() -> any:
        return api.model('Error 400', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=400)
        })
    
    @staticmethod
    def error_model() -> any:
        return api.model('Error 404', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=404)
        })
    
    @staticmethod
    def error_model() -> any:
        return api.model('Error 500', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=500)
        })
