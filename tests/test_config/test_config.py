def test_config_openai():
    from src.config import settings

    assert settings.openai.api_key.get_secret_value().startswith("sk-")


def test_config_llm():
    from src.config import settings

    assert settings.llm.model.startswith("gpt")
    assert settings.llm.model_small.startswith("gpt")
