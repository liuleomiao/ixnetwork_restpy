def test_can_add_remove_containers (config_assistant):
    config_assistant.config.Vport.add().add()
    config_assistant.commit()
    vports = config_assistant.config.Vport.find()
    assert(len(vports) == 2)

    vports.remove()
    config_assistant.commit()

    assert(len(config_assistant.config.Vport.find()) == 0)

