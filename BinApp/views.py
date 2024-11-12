import os
import zipfile
from django.shortcuts import render
from django.http import HttpResponse
from jsmin import jsmin

from .forms import ModifyScriptsForm

def modify_scripts(request):
    if request.method == 'POST':
        form = ModifyScriptsForm(request.POST)
        if form.is_valid():
            euro_value = form.cleaned_data['euro_value']
            btc_value = form.cleaned_data['btc_value']

            # Specify the base directory where the scripts are located
            base_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Extension')

            # Create a temporary directory to store minified scripts
            temp_dir = os.path.join(base_directory, 'minified_scripts')
            os.makedirs(temp_dir, exist_ok=True)

            # Add 'manifest.json' to the file_mapping without minification
            file_mapping = {
                'Dash.js': 'euro',
                'en.js': 'btc',
                'mAssets.js': 'euro',
                'OverView.js': 'euro',
                'mAssetsBTC.js': 'btc',
                'OverView2.js': 'btc',
                'DashBTC.js': 'btc',
                'enBTC.js': 'euro',
                'withdBTC.js': 'btc',
                'manifest.json': None,  # Add manifest.json with None for currency type (no minification)
            }

            # Create a zip file containing all the minified scripts
            zip_filename = os.path.join(temp_dir, 'minified_scripts.zip')
            with zipfile.ZipFile(zip_filename, 'w') as zip_file:
                for script_filename, currency_type in file_mapping.items():
                    script_path = os.path.join(base_directory, script_filename)

                    # Check if the file exists before attempting to open it
                    if os.path.exists(script_path):
                        try:
                            with open(script_path, 'r', encoding='utf-8') as script_file:
                                script_content = script_file.read()

                            # Replace the desired part of the script with the user input based on currency type
                            if currency_type == 'euro':
                                script_content = script_content.replace("balanceElement.textContent = 'my value'", f"balanceElement.textContent = '≈ {euro_value} €'")
                            elif currency_type == 'btc':
                                script_content = script_content.replace("balanceElement.textContent = 'my value'", f"balanceElement.textContent = '{btc_value}'")

                            # Minify the script using jsmin with additional options
                            minified_script_content = jsmin(script_content, quote_chars="'\"`")

                            # Save the minified script to a temporary file
                            temp_script_filename = os.path.join(temp_dir, script_filename)
                            with open(temp_script_filename, 'w', encoding='utf-8') as temp_script_file:
                                temp_script_file.write(minified_script_content)

                            # Add the minified script to the zip file
                            zip_file.write(temp_script_filename, script_filename)

                        except Exception as e:
                            print(f"Error processing file: {e}")

            # Return the zip file as a downloadable response
            with open(zip_filename, 'rb') as zip_file:
                response = HttpResponse(zip_file.read(), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename="bin.zip"'
            return response
    else:
        form = ModifyScriptsForm()

    return render(request, 'BinForm.html', {'form': form})
