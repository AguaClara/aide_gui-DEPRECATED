#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Hello addin')
        
        # Set styles of file dialog.
        fileDlg = ui.createFileDialog()
        fileDlg.isMultiSelectEnabled = True
        fileDlg.title = 'Fusion File Dialog'
        fileDlg.filter = '*.*'

        # Show file open dialog
        dlgResult = fileDlg.showOpen()
        if dlgResult == adsk.core.DialogResults.DialogOK:
            msg += '\nopen files:'
            for filename in fileDlg.filenames:
                msg += '\n\t{}'.format(filename)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Stop addin')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
