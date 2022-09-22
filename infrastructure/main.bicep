param appName string = 'fnapp${uniqueString(resourceGroup().id)}'

@description('Storage Account Type')
@allowed([
  'Standard_LRS'
  'Standard_GRS'
  'Standard_RAGRS'
])
param storageAccountType string = 'Standard_LRS'
param location string =  resourceGroup().location

@description('The language worker runtime to load in the function app.')
@allowed([
  'node'
  'dotnet'
  'java'
  'python'
])
param runtime string = 'python'

var functionAppName = '${appName}azfunction'
var hostingPlanName = '${appName}azhostingplan'
var applicationInsightsName = '${appName}azappinsights'
var storageAccountName = '${uniqueString(resourceGroup().id)}azfunctions'
var workerRuntime = runtime

resource storageAccount 'Microsoft.Storage/storageAccounts@2022-05-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: storageAccountType
  }
  kind: 'Storage'
}

var accountName = storageAccount.name
var key = listKeys(storageAccount.id, storageAccount.apiVersion).keys[0].value
var endpointSuffix = environment().suffixes.storage
var storageAccountConnectionString = 'DefaultEndpointsProtocol=https;AccountName=${accountName};EndpointSuffix=${endpointSuffix};AccountKey=${key}'

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: applicationInsightsName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  } 
}

var azAppInsightsInstrumentationKey = appInsights.properties.InstrumentationKey

@description('Create the hosting plan')
resource hostingPlan 'Microsoft.Web/serverfarms@2021-01-15' = {
  name: hostingPlanName
  location: location
  kind: 'linux'
  sku: {
    name: 'S1'
  }
  properties: {
    reserved: true
  }
}

resource functionApp 'Microsoft.Web/sites@2022-03-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp'
  properties: {
    serverFarmId: hostingPlan.id
  }
}

var function_extension_version = '~4'
param 

resource appSettings 'Microsoft.Web/sites/config@2022-03-01' = {
  parent: functionApp
  name: 'appsettings'
  properties: {
    APPLICATIONINSIGHTS_CONNECTION_STRING: 'InstrumentationKey=${azAppInsightsInstrumentationKey}'
    APPLICATIONINSIGHTS_INSTRUMENTATIONKEY: azAppInsightsInstrumentationKey
    AZURE_STORAGE_CONNECTION_STRING: storageAccountConnectionString
    AzureWebJobsStorage: storageAccountConnectionString
    FUNCTIONS_WORKER_RUNTIME: workerRuntime
    FUNCTIONS_EXTENSION_VERSION: function_extension_version
    WEBSITE_CONTENTAZUREFILECONNECTIONSTRING: storageAccountConnectionString
    WEBSITE_CONTENTSHARE: '${functionAppName}-content'

  }
}
