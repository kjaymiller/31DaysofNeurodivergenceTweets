
@description('Generated from /subscriptions/9bc6238c-8d31-4efb-bbf2-c4f71526e57b/resourceGroups/31daysofndtweets/providers/Microsoft.Storage/storageAccounts/31daysofndtweets')
resource daysofndtweets 'Microsoft.Storage/storageAccounts@2022-05-01' = {
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'Storage'
  name: '31daysofndtweets'
  location: 'westus'
  tags: {
  }
  properties: {
    minimumTlsVersion: 'TLS1_0'
    allowBlobPublicAccess: true
    networkAcls: {
      bypass: 'AzureServices'
      virtualNetworkRules: []
      ipRules: []
      defaultAction: 'Allow'
    }
    supportsHttpsTrafficOnly: true
    encryption: {
      services: {
        file: {
          keyType: 'Account'
          enabled: true
        }
        blob: {
          keyType: 'Account'
          enabled: true
        }
      }
      keySource: 'Microsoft.Storage'
    }
  }
}
