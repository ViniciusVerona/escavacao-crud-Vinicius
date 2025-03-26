from database import SessionLocal, init_db
from schemas import ExcavationPointCreate
from crud import create_point, get_all_points, update_point, delete_point, get_point_by_id

init_db()
db = SessionLocal()

def menu():
    while True:
        print("\n--- MENU ESCAVAÇÃO ---")
        print("1. Cadastrar ponto")
        print("2. Listar pontos")
        print("3. Atualizar ponto")
        print("4. Remover ponto")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                ponto = ExcavationPointCreate(
                    point_type=input("Tipo: "),
                    latitude=float(input("Latitude: ")),
                    longitude=float(input("Longitude: ")),
                    altitude=float(input("Altitude: ")),
                    srid=input("SRID: "),
                    description=input("Descrição: "),
                    registered_by=input("Responsável: ")
                )
                create_point(db, ponto)
                print("✅ Registro criado!")
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            pontos = get_all_points(db)
            for p in pontos:
                print(f"[{p.id}] {p.point_type} - ({p.latitude}, {p.longitude}) - {p.description}")

        elif opcao == "3":
            try:
                id_ponto = int(input("ID do ponto: "))
                ponto = get_point_by_id(db, id_ponto)
                if not ponto:
                    print("❌ Registro não encontrado.")
                    continue
                updates = {}
                for campo in ['point_type', 'latitude', 'longitude', 'altitude', 'srid', 'description', 'registered_by']:
                    valor = input(f"{campo} (atual: {getattr(ponto, campo)}): ")
                    if valor:
                        updates[campo] = float(valor) if campo in ['latitude', 'longitude', 'altitude'] else valor
                update_point(db, id_ponto, updates)
                print("✅ Atualizado.")
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "4":
            try:
                id_ponto = int(input("ID do ponto a remover: "))
                if delete_point(db, id_ponto):
                    print("✅ Removido.")
                else:
                    print("❌ Não encontrado.")
            except:
                print("❌ Entrada inválida.")

        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()
