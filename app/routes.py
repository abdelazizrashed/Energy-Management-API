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
    from .energy_seu import register_routes as attach_energy_seu
    from .energy_consumtion_per_month import register_routes as attach_monthly_consumtion
    from .annual_trends import register_routes as attach_annual_trends

    attach_energy_sources(api)
    attach_energy_units(api)
    attach_drivers(api)
    attach_energy_seu(api)
    attach_monthly_consumtion(api)
    attach_annual_trends(api)
    # attach_events(app, api)
    # attach_reminders(app, api)
    # attach_shared(app, api)
    # attach_tasks(app, api)