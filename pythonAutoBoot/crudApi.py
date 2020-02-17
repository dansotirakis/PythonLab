import shutil
from six.moves import input

# --Variavles
inputEntity = input("Entity   : ")
inputMigration = input("Migration Number  : ")

entityName = inputEntity.title().replace(" ", "")
entityNameMessage = inputEntity.title()
entityMigration = inputEntity.replace(" ", "_").lower()
migrationName = "V" + inputMigration + "__create_table_en_" + entityMigration

# --Directories
directoryRoot = "/home/damianossotirakis/__Zallpy/"
directoryResource = directoryRoot + "__res/"
directoryRootCode = directoryRoot + "__tlog/"
directoryFolder = "java/br/com/ticketlog/booking/microservice/"
directoryFolderPromotion = directoryFolder + "promotion/"
directoryFolderEstablishment = directoryFolder + "establishment/"

# --Templates
directoryResourcePromotion = directoryResource + "structurePromoAPI/"
directoryResourceEstablishment = directoryResource + "structureAPI/"

# --ApiPromotion
directoryApiPromotion = directoryRootCode + "portaloficinas-api-promo/src/"
directoryApiPromotionCode = directoryApiPromotion + "main/" + directoryFolderPromotion
directoryApiPromotionResource = directoryApiPromotion + "main/resources/"
directoryApiPromotionMigration = directoryApiPromotionResource + "db/migration/"
directoryApiPromotionTest = directoryApiPromotion + "test/" + directoryFolderPromotion
directoryApiPromotionTestController = directoryApiPromotionTest + "controller/"

# --ApiEstablishment
directoryApiEstablishment = directoryRootCode + "portaloficinas-api-establishment/src/"
directoryApiEstablishmentCode = (
    directoryApiEstablishment + "main/" + directoryFolderEstablishment
)
directoryApiEstablishmentResource = directoryApiEstablishment + "main/resources/"
directoryApiEstablishmentMigration = directoryApiEstablishmentResource + "db/migration/"
directoryApiEstablishmentTest = (
    directoryApiEstablishment + "test/" + directoryFolderEstablishment
)
directoryApiEstablishmentTestController = directoryFolderEstablishment + "controller/"

# --CommonService
directoryCommon = (
    directoryRootCode
    + "portaloficinas-common-objects/src/main/"
    + directoryFolder
    + "/common/"
)
directoryDtoPromotion = directoryCommon + "dto/promotion/"
directoryDtoEstablishment = directoryCommon + "dto/establishment/"


def append_multiple_lines(file_name, lines_to_append):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        appendEOL = False
        # Move read cursor to the start of file.
        file_object.seek(0)
        # Check if file is not empty
        data = file_object.read(100)
        if len(data) > 0:
            appendEOL = True
        # Iterate over each string in the list
        for line in lines_to_append:
            # If file is not empty then append '\n' before first line for
            # other lines always append '\n' before appending line
            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            # Append element at the end of file
            file_object.write(line)


# -- Promotion ABCD method
def create_promotion_be(en_name, migration, en_migration):
    # -- Migration
    print("Create migration: " + migration)
    shutil.copyfile(
        directoryResourcePromotion + "XX_migration_default.sql",
        directoryApiPromotionMigration + migration + ".sql",
    )
    with open(directoryApiPromotionMigration + migration + ".sql") as f:
        newText = f.read().replace("deffault", en_migration)
    with open(directoryApiPromotionMigration + migration + ".sql", "w") as fileLoop:
        fileLoop.write(newText)
    # -- Constant
    constName = en_migration.replace("_", "-") + "s"
    print("Create constant endPoint: " + en_migration.upper() + " to " + constName)
    with open(directoryApiPromotionCode + "constant/ResourceName.java") as f:
        newText = f.read().replace("}", " ")
    with open(
        directoryApiPromotionCode + "constant/ResourceName.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    lines = [
        "  public static final String "
        + en_migration.upper()
        + ' = "'
        + constName
        + '"',
        "",
        "}",
    ]
    append_multiple_lines(
        directoryApiPromotionCode + "constant/ResourceName.java", lines
    )
    # -- Message-i18n
    print("Create Messages i18n")
    with open(directoryApiPromotionCode + "i18n/Messages.java") as f:
        newText = f.read().replace("}", " ")
    with open(directoryApiPromotionCode + "i18n/Messages.java", "w") as fileLoop:
        fileLoop.write(newText)
    lines = [
        "  public static final String ERROR_"
        + en_migration.upper()
        + '_NOT_FOUND ="ERROR_'
        + en_migration.upper()
        + '_NOT_FOUND";',
        "  public static final String ERROR_"
        + en_migration.upper()
        + '_TITLE_CANNOT_BE_EMPTY = "ERROR_'
        + en_migration.upper()
        + '_TITLE_CANNOT_BE_EMPTY";',
        "  public static final String ERROR_"
        + en_migration.upper()
        + '_TITLE_MAX_LIMIT_SIZE = "ERROR_'
        + en_migration.upper()
        + '_TITLE_MAX_LIMIT_SIZE";',
        "  public static final String ERROR_"
        + en_migration.upper()
        + "_DESCRIPTION_CANNOT_BE_EMPTY =",
        '      "ERROR_' + en_migration.upper() + '_DESCRIPTION_CANNOT_BE_EMPTY";',
        "  public static final String ERROR_"
        + en_migration.upper()
        + "_DESCRIPTION_MAX_LIMIT_SIZE =",
        '      "ERROR_' + en_migration.upper() + '_DESCRIPTION_MAX_LIMIT_SIZE";' "",
        "}",
    ]
    append_multiple_lines(directoryApiPromotionCode + "i18n/Messages.java", lines)
    # -- Message-es
    print("Create message es: ")
    with open(directoryApiPromotionResource + "message_es.properties") as f:
        newText = f.read().replace("}", " ")
    with open(directoryApiPromotionResource + "message_es.properties", "w") as fileLoop:
        fileLoop.write(newText)
    lines = [
        "#",
        "#" + en_name,
        "#",
        "ERROR_" + en_migration.upper() + "_NOT_FOUND=Registro no encontrado",
        "ERROR_"
        + en_migration.upper()
        + "_TITLE_CANNOT_BE_EMPTY="
        + entityNameMessage
        + " el t\u00ectulo es obligatorio y debe llenarse",
        "ERROR_"
        + en_migration.upper()
        + "_TITLE_MAX_LIMIT_SIZE="
        + entityNameMessage
        + " el t\u00ectulo debe tener menos de 50 caracteres",
        "ERROR_"
        + en_migration.upper()
        + "_DESCRIPTION_CANNOT_BE_EMPTY="
        + entityNameMessage
        + " la descripci\u00f3n es obligatoria y debe completarse!",
        "ERROR_"
        + en_migration.upper()
        + "_DESCRIPTION_MAX_LIMIT_SIZE="
        + entityNameMessage
        + " la descripci\u00f3n debe tener menos de 180 caracteres"
        + "",
        "}",
    ]
    append_multiple_lines(
        directoryApiPromotionResource + "message_es.properties", lines
    )
    # -- Message-en
    print("Create message en: ")
    with open(directoryApiPromotionResource + "message.properties") as f:
        newText = f.read().replace("}", " ")
    with open(directoryApiPromotionResource + "message.properties", "w") as fileLoop:
        fileLoop.write(newText)
    lines = [
        "#",
        "#" + en_name,
        "#",
        "ERROR_" + en_migration.upper() + "_NOT_FOUND=Record not found",
        "ERROR_"
        + en_migration.upper()
        + "_TITLE_CANNOT_BE_EMPTY="
        + entityNameMessage
        + " title is mandatory and must be filled",
        "ERROR_"
        + en_migration.upper()
        + "_TITLE_MAX_LIMIT_SIZE="
        + entityNameMessage
        + " title must be less than 50 characters",
        "ERROR_"
        + en_migration.upper()
        + "_DESCRIPTION_CANNOT_BE_EMPTY="
        + entityNameMessage
        + " description is mandatory and must be filled!",
        "ERROR_"
        + en_migration.upper()
        + "_DESCRIPTION_MAX_LIMIT_SIZE="
        + entityNameMessage
        + " description must be less than 180 characters"
        + "",
        "}",
    ]
    append_multiple_lines(directoryApiPromotionResource + "message.properties", lines)
    # -- Message-en
    print("Create message pt: ")
    with open(directoryApiPromotionResource + "message_pt.properties") as f:
        newText = f.read().replace("}", " ")
    with open(directoryApiPromotionResource + "message_pt.properties", "w") as fileLoop:
        fileLoop.write(newText)
    lines = [
        "#",
        "#" + en_name,
        "#",
        "ERROR_" + en_migration.upper() + "_NOT_FOUND=Registro n\u00E3o encontrado",
        "ERROR_"
        + en_migration.upper()
        + "_TITLE_CANNOT_BE_EMPTY="
        + entityNameMessage
        + " T\u00EDtulo do "
        + entityNameMessage.lower()
        + " obrigat\u00F3rio!",
        "ERROR_"
        + en_migration.upper()
        + "_TITLE_MAX_LIMIT_SIZE="
        + entityNameMessage
        + " T\u00EDtulo do "
        + entityNameMessage.lower()
        + " deve ter menos de 50 caracteres",
        "ERROR_"
        + en_migration.upper()
        + "_DESCRIPTION_CANNOT_BE_EMPTY="
        + entityNameMessage
        + " Descri\u00E7\u00E3o do "
        + entityNameMessage.lower()
        + " \u00E9 obrigat\u00F3ria!",
        "ERROR_"
        + en_migration.upper()
        + "_DESCRIPTION_MAX_LIMIT_SIZE="
        + entityNameMessage
        + " Descri\u00E7\u00E3o do "
        + entityNameMessage.lower()
        + " deve ter menos de 180 caracteres"
        + "",
        "}",
    ]
    append_multiple_lines(
        directoryApiPromotionResource + "message_pt.properties", lines
    )
    # -- Model
    print("Create model: " + en_name)
    shutil.copyfile(
        directoryResourcePromotion + "ModelDefault.java",
        directoryApiPromotionCode + "model/" + en_name + ".java",
    )
    with open(directoryApiPromotionCode + "model/" + en_name + ".java") as f:
        newText = f.read().replace("deffault", en_migration)
    with open(
        directoryApiPromotionCode + "model/" + en_name + ".java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    with open(directoryApiPromotionCode + "model/" + en_name + ".java") as f:
        newText = f.read().replace("Deffault", en_name)
    with open(
        directoryApiPromotionCode + "model/" + en_name + ".java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    with open(directoryApiPromotionCode + "model/" + en_name + ".java") as f:
        newText = f.read().replace("DEFFAULT", en_name.upper())
    with open(
        directoryApiPromotionCode + "model/" + en_name + ".java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    # -- Repository
    print("Create repository: " + en_name + "Repository")
    shutil.copyfile(
        directoryResourcePromotion + "RepositoryDefault.java",
        directoryApiPromotionCode + "repository/" + en_name + "Repository.java",
    )
    with open(
        directoryApiPromotionCode + "repository/" + en_name + "Repository.java"
    ) as f:
        newText = f.read().replace("Deffault", en_name)
    with open(
        directoryApiPromotionCode + "repository/" + en_name + "Repository.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    with open(
        directoryApiPromotionCode + "repository/" + en_name + "Repository.java"
    ) as f:
        newText = f.read().replace("deffault", en_name.lower())
    with open(
        directoryApiPromotionCode + "repository/" + en_name + "Repository.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    # -- Service
    print("Create service: " + en_name + "Service")
    shutil.copyfile(
        directoryResourcePromotion + "ServiceDefault.java",
        directoryApiPromotionCode + "service/" + en_name + "Service.java",
    )
    with open(directoryApiPromotionCode + "service/" + en_name + "Service.java") as f:
        newText = f.read().replace("Deffault", en_name)
    with open(
        directoryApiPromotionCode + "service/" + en_name + "Service.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    with open(directoryApiPromotionCode + "service/" + en_name + "Service.java") as f:
        newText = f.read().replace("deffault", en_name.lower())
    with open(
        directoryApiPromotionCode + "service/" + en_name + "Service.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    with open(directoryApiPromotionCode + "service/" + en_name + "Service.java") as f:
        newText = f.read().replace("DEFFAULT", en_name.upper())
    with open(
        directoryApiPromotionCode + "service/" + en_name + "Service.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    # -- Controller
    print("Create repository: " + en_name + "Repository")
    shutil.copyfile(
        directoryResourcePromotion + "ControllerDefault.java",
        directoryApiPromotionCode + "controller/" + en_name + "Controller.java",
    )
    with open(
        directoryApiPromotionCode + "controller/" + en_name + "Controller.java"
    ) as f:
        newText = f.read().replace("Deffault", en_name)
    with open(
        directoryApiPromotionCode + "controller/" + en_name + "Controller.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    with open(
        directoryApiPromotionCode + "controller/" + en_name + "Controller.java"
    ) as f:
        newText = f.read().replace("deffault", en_name.lower())
    with open(
        directoryApiPromotionCode + "controller/" + en_name + "Controller.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    with open(
        directoryApiPromotionCode + "controller/" + en_name + "Controller.java"
    ) as f:
        newText = f.read().replace("DEFFAULT", en_migration.upper())
    with open(
        directoryApiPromotionCode + "controller/" + en_name + "Controller.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    # -- Test controller
    print("Create controller test: " + en_name + "ControllerTest")
    shutil.copyfile(
        directoryResourcePromotion + "ControllerTestDefault.java",
        directoryApiPromotionTestController + en_name + "ControllerTest.java",
    )
    with open(
        directoryApiPromotionTestController + en_name + "ControllerTest.java"
    ) as f:
        newText = f.read().replace("Deffault", en_name)
    with open(
        directoryApiPromotionTestController + en_name + "ControllerTest.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    with open(
        directoryApiPromotionTestController + en_name + "ControllerTest.java"
    ) as f:
        newText = f.read().replace("deffault", en_name.lower())
    with open(
        directoryApiPromotionTestController + en_name + "ControllerTest.java", "w"
    ) as fileLoop:
        fileLoop.write(newText)
    # -- DTO
    print("Create DTOs: " + en_name + "DTO " + en_name + "ListDTO")
    shutil.copyfile(
        directoryResourcePromotion + "DefaultDTO.java",
        directoryDtoPromotion + en_name + "DTO.java",
    )
    shutil.copyfile(
        directoryResourcePromotion + "DefaultListDTO.java",
        directoryDtoPromotion + en_name + "DTOList.java",
    )
    with open(directoryDtoPromotion + en_name + "DTOList.java") as f:
        newText = f.read().replace("Deffault", en_name)
    with open(directoryDtoPromotion + en_name + "DTOList.java", "w") as fileLoop:
        fileLoop.write(newText)
    with open(directoryDtoPromotion + en_name + "DTO.java") as f:
        newText = f.read().replace("Deffault", en_name)
    with open(directoryDtoPromotion + en_name + "DTO.java", "w") as fileLoop:
        fileLoop.write(newText)
    with open(directoryDtoPromotion + en_name + "DTOList.java") as f:
        newText = f.read().replace("deffault", en_name.lower())
    with open(directoryDtoPromotion + en_name + "DTOList.java", "w") as fileLoop:
        fileLoop.write(newText)
    with open(directoryDtoPromotion + en_name + "DTO.java") as f:
        newText = f.read().replace("deffault", en_name.lower())
    with open(directoryDtoPromotion + en_name + "DTO.java", "w") as fileLoop:
        fileLoop.write(newText)


# -- ABCD
create_promotion_be(entityName, migrationName, entityMigration)
