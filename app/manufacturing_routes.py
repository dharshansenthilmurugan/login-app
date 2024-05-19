
from fastapi import APIRouter, HTTPException
from app.models import Inventory , Machines , MaintenanceSchedule , ProductionData, QualityReport
from app.database import execute_query, fetch_one, fetch_all

router = APIRouter()

@router.post("/machines/create")
async def create_machines(machines: Machines):
    print("inside function")
    query = """
        INSERT INTO machines (machine_id, status)
        VALUES ($1, $2)
    """
    print("query", query)
    try:
        await execute_query(query, machines.machine_id, machines.status)
        return {"message": "Machine created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/machines/read_all")
async def read_all_machines():
    query = """
        SELECT * FROM machines
    """
    try:
        machines = await fetch_all(query)
        return machines
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/machines/{machine_id}")
async def read_one_machine(machine_id: int):
    query = """
        SELECT * FROM machines
        WHERE machine_id = $1
    """
    result = await fetch_one(query, machine_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Machine not found")

@router.put("/machines/{machine_id}")
async def update_machine(machine_id: int, machines: Machines):
    print("machines inside")
    query_update = """
        UPDATE machines
        SET status = $1
        WHERE machine_id = $2
    """
    query_select = """
        SELECT * FROM machines
        WHERE machine_id = $1
    """
    print("queries", query_update, query_select)
    try:
        await execute_query(query_update, machines.status, machine_id)
        updated_machine = await fetch_one(query_select, machine_id)
        print("updated machine", update_machine)
        return {"message": "Machine updated successfully", "machine": updated_machine}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.delete("/machines/delete/{machine_id}")
async def delete_machines(machine_id: int):
    query = """
        DELETE FROM machines
        WHERE machine_id = $1
    """
    try:
        await execute_query(query, machine_id)
        return {"message": "machine deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")




@router.post("/inventoryItem/create")
async def create_inventoryItem(inventory: Inventory):
    print("inside function")
    query = """
        INSERT INTO inventory (item_id,name,quantity)
        VALUES ($1, $2,$3)
    """
    print("query", query)
    try:
        await execute_query(query, inventory.item_id, inventory.name,inventory.quantity)
        return {"message": "inventoryItem created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/inventory/read_all")
async def read_all_inventory():
    print("inside function")
    query = """
        SELECT * FROM inventory
    """
    try:
        inventory = await fetch_all(query)
        return inventory
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/inventory/{item_id}")
async def read_one_inventory(item_id: int):
    query = """
        SELECT * FROM inventory
        WHERE item_id = $1
    """
    result = await fetch_one(query, item_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="inventory not found")

@router.put("/inventory/{item_id}")
async def update_inventory(item_id: int, inventory: Inventory):
    print("inventory inside")
    query_update = """
        UPDATE inventory
        SET name = $1, quantity = $2
        WHERE item_id = $3
    """
    query_select = """
        SELECT * FROM inventory
        WHERE item_id = $1
    """
    print("queries", query_update, query_select)
    try:
        await execute_query(query_update, inventory.name, inventory.quantity, item_id)
        updated_item = await fetch_one(query_select, item_id)
        print("updated item", updated_item)
        return {"message": "Inventory  updated successfully", "inventory": updated_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.delete("/inventory/delete/{item_id}")
async def delete_inventory(item_id: int):
    query = """
        DELETE FROM inventory
        WHERE item_id = $1
    """
    try:
        await execute_query(query, item_id)
        return {"message": "inventory deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/productiondata/create")
async def create_productiondata(production_data: ProductionData):
    print("inside function")
    query = """
        INSERT INTO productiondata (id, machine_id, product_id, quantity, timestamp)
        VALUES ($1, $2, $3, $4, $5)
    """
    print("query", query)
    try:
        await execute_query(query, production_data.id, production_data.machine_id, production_data.product_id, production_data.quantity, production_data.timestamp)
        return {"message": "Production data created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 


@router.get("/productiondata/read_all")
async def read_all_productiondata():
    print("inside function")
    query = """
        SELECT * FROM productiondata
    """
    try:
        productiondata = await fetch_all(query)
        return productiondata
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/productiondata/{id}", response_model=ProductionData)
async def read_one_production_data(id: int):
    query = """
        SELECT * FROM productiondata
        WHERE id = $1
    """
    result = await fetch_one(query, id)
    if result:
        return ProductionData(**result)
    else:
        raise HTTPException(status_code=404, detail="Production data not found")

@router.put("/productiondata/{id}")
async def update_production_data(id: int, production_data: ProductionData):
    query_update = """
        UPDATE productiondata
        SET machine_id = $1, product_id = $2, quantity = $3, timestamp = $4
        WHERE id = $5
    """
    query_select = """
        SELECT * FROM productiondata
        WHERE id = $1
    """
    try:
        await execute_query(query_update, production_data.machine_id, production_data.product_id, production_data.quantity, production_data.timestamp, id)
        updated_item = await fetch_one(query_select, id)
        return {"message": "Production data updated successfully", "production_data": updated_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.delete("/productiondata/delete/{id}")
async def delete_productiondata(id: int):
    query = """
        DELETE FROM productiondata
        WHERE id = $1
    """
    try:
        await execute_query(query, id)
        return {"message": "productiondata deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.post("/qualityreport/create")
async def create_qualityreport(qualityreport: QualityReport):
    print("inside function")
    query = """
        INSERT INTO qualityreport (report_id, machine_id, issues_found, timestamp)
        VALUES ($1, $2, $3, $4)
    """
    print("query", query)
    try:
        await execute_query(query, qualityreport.report_id, qualityreport.machine_id, qualityreport.issues_found, qualityreport.timestamp)
        return {"message": "QualityReport created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/qualityreport/read_all")
async def read_all_qualityreports():
    print("inside function")
    query = """
        SELECT * FROM qualityreport
    """
    try:
        qualityreports = await fetch_all(query)
        return qualityreports
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/qualityreport/{report_id}", response_model=QualityReport)
async def read_one_quality_report(report_id: int):
    query = """
        SELECT * FROM qualityreport
        WHERE report_id = $1
    """
    result = await fetch_one(query, report_id)
    if result:
        return QualityReport(**result)
    else:
        raise HTTPException(status_code=404, detail="Quality report not found")  

@router.put("/qualityreport/{id}")
async def update_quality_report(id: int, quality_report: QualityReport):
    query_update = """
        UPDATE qualityreport
        SET machine_id = $1, issues_found = $2, timestamp = $3
        WHERE report_id = $4
    """
    query_select = """
        SELECT * FROM qualityreport
        WHERE report_id = $1
    """
    try:
        await execute_query(query_update, quality_report.machine_id, quality_report.issues_found, quality_report.timestamp, id)
        updated_item = await fetch_one(query_select, id)
        return {"message": "Quality report updated successfully", "quality_report": updated_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.delete("/qualityreport/delete/{report_id}")
async def delete_quality_report(report_id: int):
    query = """
        DELETE FROM qualityreport
        WHERE report_id = $1
    """
    try:
        await execute_query(query, report_id)
        return {"message": "Quality report deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/maintenanceschedule/create")
async def create_maintenanceschedule(maintenanceschedule: MaintenanceSchedule):
    print("inside function")
    query = """
        INSERT INTO maintenanceschedule (id, machine_id, scheduled_date, description)
        VALUES ($1, $2, $3, $4)
    """
    print("query", query)
    try:
        await execute_query(query, maintenanceschedule.id, maintenanceschedule.machine_id, maintenanceschedule.scheduled_date, maintenanceschedule.description)
        return {"message": "Maintenance schedule created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")  


@router.get("/maintenanceschedule/read_all")
async def read_all_maintenanceschedules():
    print("inside function")
    query = """
        SELECT * FROM maintenanceschedule
    """
    try:
        maintenanceschedules = await fetch_all(query)
        return maintenanceschedules
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/maintenanceschedule/{id}", response_model=MaintenanceSchedule)
async def read_one_maintenance_schedule(id: int):
    query = """
        SELECT * FROM maintenanceschedule
        WHERE id = $1
    """
    result = await fetch_one(query, id)
    if result:
        return MaintenanceSchedule(**result)
    else:
        raise HTTPException(status_code=404, detail="Maintenance schedule not found")


@router.put("/maintenanceschedule/{id}")
async def update_maintenance_schedule(id: int, maintenance_schedule: MaintenanceSchedule):
    query_update = """
        UPDATE maintenanceschedule
        SET machine_id = $1, scheduled_date = $2, description = $3
        WHERE id = $4
    """
    query_select = """
        SELECT * FROM maintenanceschedule
        WHERE id = $1
    """
    try:
        await execute_query(query_update, maintenance_schedule.machine_id, maintenance_schedule.scheduled_date, maintenance_schedule.description, id)
        updated_item = await fetch_one(query_select, id)
        return {"message": "Maintenance schedule updated successfully", "maintenance_schedule": updated_item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")



@router.delete("/maintenanceschedule/delete/{id}")
async def delete_maintenanceschedule(id: int):
    query = """
        DELETE FROM maintenanceschedule
        WHERE id = $1
    """
    try:
        await execute_query(query, id)
        return {"message": "Maintenance schedule deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


        



