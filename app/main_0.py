from nicegui import ui


@ui.page('/')
def principal()->None:
    ui.query('body').classes('bg-amber-100')
    with ui.row().classes('items-center'):
        ui.image('../img/logo_farol_na_quebrada-removebg.png').classes('w-24')
        ui.label('Bem-vindos ao Farol na quebrada').classes('text-lg text-orange-500')
        

ui.run(title="Minha primeira pagina web em python", 
       language='pt-BR', favicon='../img/logo_farol_na_quebrada.jpg')