def register_routes(api,):
    pass
    # from .auth import register_routes as attach_auth
    # from .events import register_routes as attach_events
    # from .reminders import  register_routes as attach_reminders
    # from .shared import register_routes as attach_shared
    # from .tasks import register_routes as attach_tasks
    from .energy_sources import register_routes as attach_energy_sources
    from .energy_units import register_routes as attach_energy_units
    from .drivers import register_routes as attach_drivers

    attach_energy_sources(api)
    attach_energy_units(api)
    attach_drivers(api)
    # attach_auth(api, app)
    # attach_events(app, api)
    # attach_reminders(app, api)
    # attach_shared(app, api)
    # attach_tasks(app, api)