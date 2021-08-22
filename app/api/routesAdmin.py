from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def welcome():
    return {
        'message': 'Bem vindo a API!',
        'endpoints': [
            {
                'docs': '/docs',
                'redocs': '/redocs',
                'users': 'users'
            }
        ]
    }
