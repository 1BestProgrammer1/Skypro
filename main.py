from flask import Flask

from utils import load_json, format_candidates, get_candidate_by_id, get_candidate_by_skill


app = Flask(__name__)


@app.route('/')
def page_main():
    """Главная страница"""
    candidates: list[dict] = load_json()
    result: str = format_candidates(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Поиск кандидата id"""
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route('/skills/<skill>')
def page_skills(skilL):
    """Поиск по навыку"""
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result


app.run()
