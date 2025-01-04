def test_config_loads():
    from src.config import settings

    assert not settings.debug

    assert settings.openai.api_key.startswith("sk-")
    assert settings.openai.llm.startswith("gpt")
    assert settings.openai.llm_small.startswith("gpt")
