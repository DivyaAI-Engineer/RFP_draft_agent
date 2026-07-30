param location string = resourceGroup().location
param containerAppName string
param containerEnvName string
param acrName string

resource acr 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: acrName
  location: location
  sku: {
    name: 'Basic'
  }
}

resource env 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: containerEnvName
  location: location
  properties: {}
}

resource app 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  properties: {
    managedEnvironmentId: env.id
    configuration: {
      ingress: {
        external: true
        targetPort: 8000
      }
      registries: [
        {
          server: '${acr.name}.azurecr.io'
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'mobility-rfp-agent'
          image: '${acr.name}.azurecr.io/mobility-rfp-agent:latest'
        }
      ]
    }
  }
}
